from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.attributes import SpecialConditions
from spirit.game.card_effects.attacks_common import condition_attack
from spirit.game.card_effects.ecard import bubble_jump


card = PokemonCardDef(
    guid="5ea3b1df-08ca-5e1c-a6e8-5cd2d5f655a0",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LightAzumarill.Name",
    display_name="Light Azumarill",
    searchable_by=["Light Azumarill", "Stage 1", "LightAzumarill"],
    subtypes=["Stage 1"],
    collector_number=13,
    set_code="NEO4",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=184,
    abilities=[
        Attack(
            title="Bubble",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.WATER: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
        Attack(
            title="Bubble Jump",
            game_text="If you have any Benched Pok\u00e9mon, flip a coin. If heads, take 2 Energy cards attached to Light Azumarill and attach them to 1 of your Benched Pok\u00e9mon. Then return Light Azumarill and all cards attached to it to your hand.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=bubble_jump,
        ),
    ],
)
