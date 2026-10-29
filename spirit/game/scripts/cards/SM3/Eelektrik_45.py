from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm3 import small_appetite

card = PokemonCardDef(
    guid="71a8385f-185a-50c2-a839-514416507464",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Eelektrik.Name",
    display_name="Eelektrik",
    searchable_by=["Eelektrik", "Stage 1", "Eelektrik"],
    subtypes=["Stage 1"],
    collector_number=45,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    family_id=602,
    abilities=[
        Attack(
            title="Small Appetite",
            game_text="If your opponent's Active Pok\u00e9mon's maximum HP is 100 or more, this attack does nothing.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=small_appetite,
        ),
    ],
)
