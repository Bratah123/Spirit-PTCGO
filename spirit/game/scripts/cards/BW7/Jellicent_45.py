from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes, SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.session.passives import Passive


class _StickinessPassive(Passive):
    """The Retreat Cost of each of your opponent's Pokemon in play is Colorless more."""

    def modify_retreat_cost(self, cost, pokemon, carrier, board):
        if pokemon.owning_player_id != carrier.owning_player_id:
            return cost + 1
        return cost


card = PokemonCardDef(
    guid="d089aace-8b5a-55f0-b25b-7ea4f1c49b72",
    key="BW7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jellicent.Name",
    display_name="Jellicent",
    searchable_by=["Jellicent", "Stage 1", "Jellicent"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="BW7",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Frillish.Name",
    family_id=592,
    abilities=[
        Ability(
            title="Stickiness",
            game_text="The Retreat Cost of each of your opponent's Pok\u00e9mon in play is Colorless more.",
            ability_type=AbilityTypes.POKE_ABILITY,
            passive=_StickinessPassive(),
        ),
        Attack(
            title="Eerie Light",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=condition_attack(SpecialConditions.CONFUSED, flip=True),
        ),
    ],
)