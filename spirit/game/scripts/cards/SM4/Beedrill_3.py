from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm4 import sudden_sting

card = PokemonCardDef(
    guid="404ba0e5-ac58-5a0a-a051-beb3c61970c7",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beedrill.Name",
    display_name="Beedrill",
    searchable_by=["Beedrill", "Stage 2", "Beedrill"],
    subtypes=["Stage 2"],
    collector_number=3,
    set_code="SM4",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kakuna.Name",
    family_id=13,
    abilities=[
        Attack(
            title="Sudden Sting",
            game_text="If this Pok\u00e9mon evolved from Kakuna during this turn, your opponent's Active Pok\u00e9mon is now Paralyzed and Poisoned.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=sudden_sting,
        ),
        Attack(
            title="Sharp Sting",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
        ),
    ],
)