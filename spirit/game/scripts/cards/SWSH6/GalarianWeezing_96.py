from spirit.game.data_utils import PokemonCardDef, Attack, Ability, def_for
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.session.passives import Passive, active_passives


def _is_weezing_named(pokemon):
    d = def_for(pokemon.archetype_id)
    return d is not None and "Weezing" in (d.display_name or "")


class EnergyFactoryPassive(Passive):
    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.DARKNESS.value):
            return options
        if not _is_weezing_named(holder):
            return options
        if any(len(option) >= 2 for option in options):
            return options
        active_here = any(
            isinstance(p, EnergyFactoryPassive) and c.owning_player_id == holder.owning_player_id
            for p, c in active_passives(board)
        )
        if not active_here:
            return options
        return [list(option) * 2 for option in options]


card = PokemonCardDef(
    guid="8b3f9833-676f-5184-a3d1-028d2a83db1d",
    key="SWSH6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalarianWeezing.Name",
    display_name="Galarian Weezing",
    searchable_by=["Galarian Weezing", "Stage 1", "GalarianWeezing"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SWSH6",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Koffing.Name",
    family_id=109,
    abilities=[
        Ability(
            title="Energy Factory",
            game_text="Each basic Darkness Energy attached to your Pok\u00e9mon that have \"Weezing\" in their name provides DarknessDarkness Energy. You can't apply more than 1 Energy Factory Ability at a time.",
            passive=EnergyFactoryPassive(),
        ),
        Attack(
            title="Suffocating Gas",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)