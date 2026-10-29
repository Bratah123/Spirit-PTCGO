from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import light_of_the_protector_gx

card = PokemonCardDef(
    guid="3b5a7290-6119-5d51-8d16-fd13672fd27e",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.SolgaleoLunalaGX.Name",
    display_name="Solgaleo & Lunala-GX",
    searchable_by=["Solgaleo & Lunala-GX", "Basic", "TAG TEAM", "GX", "SolgaleoLunalaGX"],
    subtypes=["Basic", "TAG TEAM", "GX"],
    collector_number=75,
    set_code="SM12",
    rarity=Rarities.RareHoloGX,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=791,
    abilities=[
        Attack(
            title="Cosmic Burn",
            game_text="This Pok\u00e9mon can't use Cosmic Burn during your next turn.",
            cost={PokemonTypes.PSYCHIC: 3, PokemonTypes.COLORLESS: 1},
            damage=230,
            locks_next_turn=True,
        ),
        Attack(
            title="Light of the Protector-GX",
            game_text="If you played Lillie's Full Force from your hand during this turn, prevent all effects of attacks, including damage, done to each of your Pok\u00e9mon during your opponent's next turn. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=light_of_the_protector_gx,
        ),
    ],
)