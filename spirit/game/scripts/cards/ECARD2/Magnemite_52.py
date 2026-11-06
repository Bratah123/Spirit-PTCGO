from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack


card = PokemonCardDef(
    guid="bf421227-7d36-543d-87b1-bb59ee5fbc2c",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magnemite.Name",
    display_name="Magnemite",
    searchable_by=["Magnemite", "Basic", "Magnemite"],
    subtypes=["Basic"],
    collector_number=52,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    family_id=81,
    abilities=[
        Attack(
            title="Attract",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon and switch the Defending Pok\u00e9mon with it.",
            cost={PokemonTypes.METAL: 1},
            effect=gust_attack(damage_before=0),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
    ],
)
