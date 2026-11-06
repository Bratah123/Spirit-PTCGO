from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import collect_energy_from_discard


card = PokemonCardDef(
    guid="0a52a06b-67cb-52c8-a8e0-d91a3974fcb0",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    display_name="Vulpix",
    searchable_by=["Vulpix", "Basic", "Vulpix"],
    subtypes=["Basic"],
    collector_number=116,
    set_code="ECARD2",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=37,
    abilities=[
        Attack(
            title="Collect Fire",
            game_text="If there are any Fire Energy cards in your discard pile, flip a coin. If heads, attach 1 of them to Vulpix.",
            cost={PokemonTypes.FIRE: 1},
            damage=10,
            effect=collect_energy_from_discard(PokemonTypes.FIRE),
        ),
    ],
)
