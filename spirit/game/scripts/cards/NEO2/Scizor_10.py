from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import false_swipe


card = PokemonCardDef(
    guid="27a6a4af-3b63-53c4-931a-a842d5cc5f0c",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name",
    display_name="Scizor",
    searchable_by=["Scizor", "Stage 1", "Scizor"],
    subtypes=["Stage 1"],
    collector_number=10,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name",
    family_id=123,
    abilities=[
        Attack(
            title="False Swipe",
            game_text="Does damage equal to half the Defending Pok\u00e9mon's remaining HP (rounded down to the nearest 10).",
            cost={PokemonTypes.METAL: 1},
            effect=false_swipe,
        ),
        Attack(
            title="Double Claw",
            game_text="Flip 2 coins. This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="+",
            effect=flip_damage(coins=2, per_heads=20),
        ),
    ],
)
