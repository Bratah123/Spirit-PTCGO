from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import damage_typed_bench


card = PokemonCardDef(
    guid="f5ae1810-6515-5b0f-a59f-416b9e5cbb7d",
    key="GYM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlainesGrowlithe.Name",
    display_name="Blaine's Growlithe",
    searchable_by=["Blaine's Growlithe", "Basic", "BlainesGrowlithe"],
    subtypes=["Basic"],
    collector_number=62,
    set_code="GYM1",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=58,
    abilities=[
        Attack(
            title="Blaze",
            game_text="Does 10 damage to each Grass Pok\u00e9mon on your opponent's Bench. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIRE: 2},
            damage=20,
            effect=damage_typed_bench(10, PokemonTypes.GRASS),
        ),
    ],
)
