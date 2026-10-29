from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus, recoil_attack


card = PokemonCardDef(
    guid="6a4dba7e-db57-5e0d-91eb-d34d83e9fff4",
    key="SM1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Decidueye.Name",
    display_name="Decidueye",
    searchable_by=["Decidueye", "Stage 2", "Decidueye"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="SM1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dartrix.Name",
    family_id=722,
    abilities=[
        Attack(
            title="Leaf Blade",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
        Attack(
            title="Brave Bird",
            game_text="This Pok\u00e9mon does 20 damage to itself.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=recoil_attack(20),
        ),
    ],
)