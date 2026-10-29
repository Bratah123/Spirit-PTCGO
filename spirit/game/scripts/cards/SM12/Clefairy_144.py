from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import doll_swap

card = PokemonCardDef(
    guid="ead9f49e-226a-58e2-b480-f7f7d936a287",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Clefairy.Name",
    display_name="Clefairy",
    searchable_by=["Clefairy", "Basic", "Clefairy"],
    subtypes=["Basic"],
    collector_number=144,
    set_code="SM12",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    family_id=35,
    abilities=[
        Attack(
            title="Doll Swap",
            game_text="Put this Pok\u00e9mon and all cards attached to it into your hand. If you do, you may play Lillie's Pok\u00e9 Doll from your hand as your new Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            effect=doll_swap,
        ),
    ],
)