from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_bonus


card = PokemonCardDef(
    guid="2c7203ee-81a8-5ec7-96cb-b3ee02efbdef",
    key="XY5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Combusken.Name",
    display_name="Combusken",
    searchable_by=["Combusken", "Stage 1", "Combusken"],
    subtypes=["Stage 1"],
    collector_number=27,
    set_code="XY5",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Torchic.Name",
    family_id=255,
    abilities=[
        Attack(
            title="Quick Attack",
            game_text="Flip a coin. If heads, this attack does 20 more damage.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            damage_operator="+",
            effect=flip_bonus(20),
        ),
        Attack(
            title="Spiral Kick",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)