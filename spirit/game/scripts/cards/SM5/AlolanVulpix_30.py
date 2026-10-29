from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="63c2a4bb-83d5-567e-96af-ab797c754642",
    key="SM5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    display_name="Alolan Vulpix",
    searchable_by=["Alolan Vulpix", "Basic", "AlolanVulpix"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="SM5",
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=37,
    abilities=[
        Attack(
            title="Roar",
            game_text="Your opponent switches their Active Pok\u00e9mon with 1 of their Benched Pok\u00e9mon.",
            cost={},
            # STUB: attack effect not implemented
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Icy Snow",
            cost={PokemonTypes.WATER: 1},
            damage=10,
        ),
    ],
)