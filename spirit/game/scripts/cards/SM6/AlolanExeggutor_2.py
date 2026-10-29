from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm6 import tropical_shake

card = PokemonCardDef(
    guid="6c47397e-deb2-5690-a8cb-c004b3e0f53b",
    key="SM6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanExeggutor.Name",
    display_name="Alolan Exeggutor",
    searchable_by=["Alolan Exeggutor", "Stage 1", "AlolanExeggutor"],
    subtypes=["Stage 1"],
    collector_number=2,
    set_code="SM6",
    rarity=Rarities.Rare,
    hp=160,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    family_id=102,
    abilities=[
        Attack(
            title="Tropical Shake",
            game_text="This attack does 20 more damage for each type of basic Energy card in your discard pile. You can't add more than 100 damage in this way.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            damage_operator="+",
            effect=tropical_shake,
        ),
    ],
)
