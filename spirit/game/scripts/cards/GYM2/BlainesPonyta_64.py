from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import hind_kick


card = PokemonCardDef(
    guid="4c856cc3-e780-50cf-a666-f17f505a7960",
    key="GYM2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesPonyta.Name",
    display_name="Blaine's Ponyta",
    searchable_by=["Blaine's Ponyta", "Basic", "BlainesPonyta"],
    subtypes=["Basic"],
    collector_number=64,
    set_code="GYM2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=77,
    abilities=[
        Attack(
            title="Hind Kick",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If heads, switch Blaine's Ponyta with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=hind_kick,
        ),
    ],
)
