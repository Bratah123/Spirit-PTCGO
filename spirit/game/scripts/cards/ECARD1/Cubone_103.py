from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_or_nothing


card = PokemonCardDef(
    guid="ce04a9e5-0e59-575c-87e1-3f5397ec3c3c",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name",
    display_name="Cubone",
    searchable_by=["Cubone", "Basic", "Cubone"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="ECARD1",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=104,
    abilities=[
        Attack(
            title="Beat",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
        Attack(
            title="Bone Smash",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=flip_or_nothing(),
        ),
    ],
)
