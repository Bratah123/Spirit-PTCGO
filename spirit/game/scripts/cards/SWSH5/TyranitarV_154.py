from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import mill_attack

card = PokemonCardDef(
    guid="2cf2263a-26d7-5bf4-9742-506c20ddad33",
    key="SWSH5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TyranitarV.Name",
    display_name="Tyranitar V",
    searchable_by=["Tyranitar V", "Basic", "V", "Single Strike", "TyranitarV"],
    subtypes=["Basic", "V", "Single Strike"],
    collector_number=154,
    set_code="SWSH5",
    rarity=Rarities.RareUltra,
    hp=230,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=248,
    abilities=[
        Attack(
            title="Cragalanche",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mill_attack(2, opponent=True),
        ),
        Attack(
            title="Single Strike Crush",
            game_text="Discard the top 4 cards of your deck.",
            cost={PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 2},
            damage=240,
            effect=mill_attack(4, opponent=False),
        ),
    ],
)
