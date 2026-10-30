from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage


card = PokemonCardDef(
    guid="fcec0c40-a61e-5690-917a-0d953e2489ce",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magikarp.Name",
    display_name="Magikarp",
    searchable_by=["Magikarp", "Basic", "Magikarp"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="BW11",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=129,
    abilities=[
        Attack(
            title="Flailing Flop",
            game_text="Flip a coin. If tails, this Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=flip_damage(tails_self_damage=10),
        ),
    ],
)