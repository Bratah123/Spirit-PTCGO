from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import recoil_attack


card = PokemonCardDef(
    guid="1a678680-2a7f-5d3b-a9c1-8c284be7179d",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rhydon.Name",
    display_name="Rhydon",
    searchable_by=["Rhydon", "Stage 1", "Rhydon"],
    subtypes=["Stage 1"],
    collector_number=75,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Rhyhorn.Name",
    family_id=111,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
            effect=recoil_attack(10),
        ),
        Attack(
            title="Horn Drill",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)