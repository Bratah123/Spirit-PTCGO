from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import squaredance


card = PokemonCardDef(
    guid="3f5207fd-d874-56b5-a823-c9233992da14",
    key="NEO1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="NEO1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=35,
    abilities=[
        Attack(
            title="Doubleslap",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Squaredance",
            game_text="Flip a number of coins equal to the total number of Pok\u00e9mon in play. For each heads, you may search your deck for a basic Energy card, show it to your opponent, and put it into your hand. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 3},
            effect=squaredance,
        ),
    ],
)
