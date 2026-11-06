from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import heads_and_tails_damage


card = PokemonCardDef(
    guid="18b34e8e-fea8-5692-af33-4519880c8fa8",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesTauros.Name",
    display_name="Blaine's Tauros",
    searchable_by=["Blaine's Tauros", "Basic", "BlainesTauros"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=128,
    abilities=[
        Attack(
            title="3-Pronged Tail",
            game_text="Flip 3 coins. This attack does 10 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="x",
            effect=flip_damage(coins=3, per_heads=10),
        ),
        Attack(
            title="Full Speed Charge",
            game_text="Flip 4 coins. This attack does 20 damage times the number of heads to the Defending Pok\u00e9mon and 20 damage times the number of tails to Blaine's Tauros.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=20,
            damage_operator="x",
            effect=heads_and_tails_damage(coins=4, per_heads=20, per_tails_self=20),
        ),
    ],
)
