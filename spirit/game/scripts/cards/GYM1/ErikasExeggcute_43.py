from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.ecard import deflector


card = PokemonCardDef(
    guid="1d0f1309-5021-5403-a38c-0e6b5fd29df1",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ErikasExeggcute.Name",
    display_name="Erika's Exeggcute",
    searchable_by=["Erika's Exeggcute", "Basic", "ErikasExeggcute"],
    subtypes=["Basic"],
    collector_number=43,
    set_code="GYM1",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=102,
    abilities=[
        Attack(
            title="Deflector",
            game_text="During your opponent's next turn, whenever Erika's Exeggcute takes damage, divide that damage in half (rounded down to the nearest 10). (Any other effects still happen.)",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=deflector,
        ),
        Attack(
            title="Egg Bomb",
            game_text="Flip a coin. If tails, this attack does nothing to the Defending Pok\u00e9mon and Erika's Exeggcute does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=flip_damage(coins=1, per_heads=40, tails_self_damage=20),
        ),
    ],
)
