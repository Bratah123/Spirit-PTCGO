from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import smokescreen_attack
from spirit.game.card_effects.ecard import thunder_attack


card = PokemonCardDef(
    guid="cdee76b3-79aa-5291-8463-bcca6b341a41",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkJolteon.Name",
    display_name="Dark Jolteon",
    searchable_by=["Dark Jolteon", "Stage 1", "DarkJolteon"],
    subtypes=["Stage 1"],
    collector_number=38,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Lightning Flash",
            game_text="If the Defending Pok\u00e9mon tries to attack during your opponent's next turn, your opponent flips a coin. If tails, that attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=20,
            effect=smokescreen_attack(),
        ),
        Attack(
            title="Thunder Attack",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed. If tails, Dark Jolteon does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=thunder_attack,
        ),
    ],
)
