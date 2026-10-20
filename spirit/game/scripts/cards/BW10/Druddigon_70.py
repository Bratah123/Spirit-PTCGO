from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing, ignore_effects_attack


card = PokemonCardDef(
    guid="8fdf1603-d7a2-5d77-858e-bd060be320bb",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Druddigon.Name",
    display_name="Druddigon",
    searchable_by=["Druddigon", "Basic", "Druddigon"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="BW10",
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=621,
    abilities=[
        Attack(
            title="Big Swing",
            game_text="Flip 2 coins. If either of them is tails, this attack does nothing.",
            cost={PokemonTypes.FIRE: 1},
            damage=40,
            effect=flip_or_nothing(coins=2),
        ),
        Attack(
            title="Shred",
            game_text="This attack's damage isn't affected by any effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=ignore_effects_attack(),
        ),
    ],
)