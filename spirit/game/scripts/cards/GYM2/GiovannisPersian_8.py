from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.attacks_common import flip_bonus
from spirit.game.card_effects.ecard import call_the_boss


card = PokemonCardDef(
    guid="65eede36-cd7c-55f9-807d-354396b2239f",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisPersian.Name",
    display_name="Giovanni's Persian",
    searchable_by=["Giovanni's Persian", "Stage 1", "GiovannisPersian"],
    subtypes=["Stage 1"],
    collector_number=8,
    set_code="GYM2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GiovannisMeowth.Name",
    family_id=52,
    abilities=[
        Ability(
            title="Call the Boss",
            game_text="When you play Giovanni's Persian from your hand, you may search your deck for the Trainer card named Giovanni, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            ability_type=AbilityTypes.POKE_POWER,
            trigger=Triggers.ON_EVOLVE,
            effect=call_the_boss,
        ),
        Attack(
            title="Ambush",
            game_text="Flip a coin. If heads, this attack does 20 damage plus 20 more damage; if tails, this attack does 20 damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
    ],
)
