from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import rototiller

card = PokemonCardDef(
    guid="b886a2f3-d519-5740-b223-1dc305d97e89",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    display_name="Drilbur",
    searchable_by=["Drilbur", "Basic", "Drilbur"],
    subtypes=["Basic"],
    collector_number=114,
    set_code="SM12",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=529,
    abilities=[
        Attack(
            title="Rototiller",
            game_text="Shuffle a card from your discard pile into your deck.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=rototiller,
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
        ),
    ],
)