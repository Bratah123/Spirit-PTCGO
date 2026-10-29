from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage

card = PokemonCardDef(
    guid="43b9752a-f1c7-5c97-beb0-92be9ad0166d",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanSandshrew.Name",
    display_name="Alolan Sandshrew",
    searchable_by=["Alolan Sandshrew", "Basic", "AlolanSandshrew"],
    subtypes=["Basic"],
    collector_number=28,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=27,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage for each heads.",
            cost={},
            damage=10,
            damage_operator="x",
            # STUB: attack effect not implemented
            effect=flip_damage(coins=3, per_heads=10),
        ),
    ],
)