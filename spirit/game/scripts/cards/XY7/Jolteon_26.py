from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID
from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.session.passives import Passive, carrier_pokemon


class _StageOneType(Passive):
    """Each of your Stage 1 Pokemon in play is now a Lightning Pokemon in addition to its types."""
    def modify_pokemon_types(self, types, pokemon, carrier):
        me = carrier_pokemon(carrier)
        if (me is None or pokemon.owning_player_id != me.owning_player_id
                or pokemon.get_attribute(AttrID.STAGE) != PokemonStage.STAGE1.value
                or PokemonTypes.LIGHTNING.value in types):
            return types
        return list(types) + [PokemonTypes.LIGHTNING.value]


card = PokemonCardDef(
    guid="e78f4e19-cf3e-5930-a33f-488d8b5c7673",
    key="XY7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jolteon.Name",
    display_name="Jolteon",
    searchable_by=["Jolteon", "Stage 1", "Jolteon"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="XY7",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Electric Effect",
            game_text="Each of your Stage 1 Pok\u00e9mon in play is now a Lightning Pok\u00e9mon in addition to its existing types.",
            passive=_StageOneType(),
        ),
        Attack(
            title="Thunder Blast",
            game_text="Discard an Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=self_energy_discard_attack(count=1),
        ),
    ],
)