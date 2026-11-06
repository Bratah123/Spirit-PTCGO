from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="0bed0e0a-ec53-51ed-869d-44ccd62e657d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BrocksLickitung.Name",
    display_name="Brock's Lickitung",
    searchable_by=["Brock's Lickitung", "Basic", "BrocksLickitung"],
    subtypes=["Basic"],
    collector_number=41,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=108,
    abilities=[
        Attack(
            title="Tongue Slap",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title="Slam",
            game_text="Flip 2 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=30),
        ),
    ],
)
