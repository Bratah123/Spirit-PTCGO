from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="4a9cda55-13f6-54f6-8969-1ab48c3af7aa",
    key="SM8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Brionne.Name",
    display_name="Brionne",
    searchable_by=["Brionne", "Stage 1", "Brionne"],
    subtypes=["Stage 1"],
    collector_number=66,
    set_code="SM8",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Popplio.Name",
    family_id=728,
    abilities=[
        Attack(
            title="Captivate",
            game_text="Switch 1 of your opponent's Benched Pok\u00e9mon with their Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1},
            effect=gust_attack(),
        ),
        Attack(
            title="Water Gun",
            cost={PokemonTypes.WATER: 1},
            damage=20,
        ),
    ],
)