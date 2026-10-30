from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import count_in_play, flip_damage


card = PokemonCardDef(
    guid="0183a22e-4b5e-53ae-95d8-76bd52b21652",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sneaselex.Name",
    display_name="Sneasel ex",
    searchable_by=["Sneasel ex", "Basic", "ex", "Sneaselex"],
    subtypes=["Basic", "ex"],
    collector_number=103,
    set_code="EX1",
    rarity=Rarities.RareHoloEX,
    hp=80,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=215,
    abilities=[
        Attack(
            title="Double Scratch",
            game_text="Flip 2 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=2, per_heads=10),
        ),
        Attack(
            title="Beat Up",
            game_text="Flip a coin for each of your Pok\u00e9mon in play (including Sneasel ex). This attack does 20 damage times the number of heads.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="x",
            effect=flip_damage(per_heads=20, coins_from=count_in_play("mine")),
        ),
    ],
)
