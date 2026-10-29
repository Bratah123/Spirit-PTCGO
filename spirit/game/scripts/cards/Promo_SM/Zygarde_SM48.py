from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import core_enforcer

card = PokemonCardDef(
    guid="5bf1ecb8-e7ff-50e2-8660-a45c7860ec4d",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zygarde.Name",
    display_name="Zygarde",
    searchable_by=["Zygarde", "Basic", "Zygarde"],
    subtypes=["Basic"],
    collector_number=48,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FAIRY,
    family_id=718,
    abilities=[
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
        Attack(
            title="Core Enforcer",
            game_text="Discard a Darkness Energy and a Fairy Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=150,
            effect=core_enforcer,
        ),
    ],
)
