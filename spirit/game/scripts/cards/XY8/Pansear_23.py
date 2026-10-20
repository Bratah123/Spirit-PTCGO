from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="98660cc4-7b1e-52b3-ad49-42fbbb25fb96",
    key="XY8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name",
    display_name="Pansear",
    searchable_by=["Pansear", "Basic", "Pansear"],
    subtypes=["Basic"],
    collector_number=23,
    set_code="XY8",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=513,
    abilities=[
        Attack(
            title="Fury Swipes",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(3, per_heads=10),
        ),
    ],
)