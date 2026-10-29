from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm12 import rubbish_blizzard

card = PokemonCardDef(
    guid="0e4c292b-ba5d-5b69-8bb2-42fee7f9b8df",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetales.Name",
    display_name="Alolan Ninetales",
    searchable_by=["Alolan Ninetales", "Stage 1", "AlolanNinetales"],
    subtypes=["Stage 1"],
    collector_number=145,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Rubbish Blizzard",
            game_text="This attack does 10 damage for each Pok\u00e9mon Tool card in your discard pile.",
            cost={},
            damage=10,
            damage_operator="x",
            effect=rubbish_blizzard,
        ),
    ],
)