from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import harden


card = PokemonCardDef(
    guid="0dc8a0d8-ec14-56fb-a08a-ffc6a6ae517e",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    display_name="Graveler",
    searchable_by=["Graveler", "Stage 1", "Graveler"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="BASE6",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Geodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Harden",
            game_text="During your opponent's next turn, whenever 30 or less damage is done to Graveler (after applying Weakness and Resistance), prevent that damage. (Any other effects of attacks still happen.)",
            cost={PokemonTypes.FIGHTING: 2},
            effect=harden(30),
        ),
        Attack(
            title="Rock Throw",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
    ],
)
