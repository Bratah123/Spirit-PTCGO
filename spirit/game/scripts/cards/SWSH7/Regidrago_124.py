from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.pokemon import dragon_energy

card = PokemonCardDef(
    guid="55f9b1ef-ad5a-5e58-851c-ae08510d3ae3",
    key="SWSH7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regidrago.Name",
    display_name="Regidrago",
    searchable_by=["Regidrago", "Basic", "Regidrago"],
    subtypes=["Basic"],
    collector_number=124,
    set_code="SWSH7",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    family_id=895,
    abilities=[
        Attack(
            title="Hammer In",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Dragon Energy",
            game_text="This attack does 20 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.FIRE: 1},
            damage=240,
            damage_operator="-",
            effect=dragon_energy,
        ),
    ],
)
