from spirit.game.card_effects.attacks_common import self_energy_discard_attack
from spirit.game.card_effects.pokemon import energy_provides_type
from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from spirit.game.session.passives import Passive, active_passives


class BurnBrightlyPassive(Passive):
    def modify_energy_provided(self, options, energy, holder, board):
        if holder is None or energy.get_attribute(AttrID.IS_SPECIAL_ENERGY):
            return options
        if not energy_provides_type(energy, PokemonTypes.FIRE.value):
            return options
        if any(len(option) >= 2 for option in options):
            return options
        active_here = any(
            isinstance(p, BurnBrightlyPassive) and c.owning_player_id == holder.owning_player_id
            for p, c in active_passives(board)
        )
        if not active_here:
            return options
        return [list(option) * 2 for option in options]


card = PokemonCardDef(
    guid="0102ad8f-c8f6-5a87-ad03-66c7fe4282b3",
    key="PGO",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Charizard.Name",
    display_name="Charizard",
    searchable_by=["Charizard", "Stage 2", "Charizard"],
    subtypes=["Stage 2"],
    collector_number=10,
    set_code="PGO",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charmeleon.Name",
    family_id=4,
    abilities=[
        Ability(
            title="Burn Brightly",
            game_text="Each basic Fire Energy attached to your Pok\u00e9mon provides FireFire Energy. You can't apply more than 1 Burn Brightly Ability at a time.",
            passive=BurnBrightlyPassive(),
        ),
        Attack(
            title="Flare Blitz",
            game_text="Discard all Fire Energy from this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 2},
            damage=170,
            effect=self_energy_discard_attack(all_energy=True, energy_type=PokemonTypes.FIRE),
        ),
    ],
)