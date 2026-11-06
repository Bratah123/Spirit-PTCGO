from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.passives_common import flip_protection


card = PokemonCardDef(
    guid="bffb4eef-9c32-5452-ad45-b4128dd12baa",
    key="NEO2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hitmontop.Name",
    display_name="Hitmontop",
    searchable_by=["Hitmontop", "Basic", "Hitmontop"],
    subtypes=["Basic"],
    collector_number=3,
    set_code="NEO2",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=237,
    abilities=[
        Attack(
            title="Detect",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all effects of attacks, including damage, done to Hitmontop.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Triple Kick",
            game_text="Flip 3 coins. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=30,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=30),
        ),
    ],
)
