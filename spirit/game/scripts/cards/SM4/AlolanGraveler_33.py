from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import self_destruct

card = PokemonCardDef(
    guid="81e69653-8a13-519c-88a7-f0d7c0ba125d",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGraveler.Name",
    display_name="Alolan Graveler",
    searchable_by=["Alolan Graveler", "Stage 1", "AlolanGraveler"],
    subtypes=["Stage 1"],
    collector_number=33,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.AlolanGeodude.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Corkscrew Punch",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Self-Destruct",
            game_text="This Pok\u00e9mon does 100 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=self_destruct,
        ),
    ],
)