from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.sm12 import scampering_tail, scampering_tail_condition

card = PokemonCardDef(
    guid="288812cc-611e-5b2a-bbf4-58bdf7e08c36",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Aipom.Name",
    display_name="Aipom",
    searchable_by=["Aipom", "Basic", "Aipom"],
    subtypes=["Basic"],
    collector_number=169,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=190,
    abilities=[
        Ability(
            title="Scampering Tail",
            game_text="Once during your turn (before your attack), you may put the top card of your opponent's deck on the bottom of their deck without looking at it.",
            ability_type=AbilityTypes.POKE_ABILITY,
            activation=Activations.ONCE_PER_TURN,
            condition=scampering_tail_condition,
            effect=scampering_tail,
        ),
        Attack(
            title="Tail Smack",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)