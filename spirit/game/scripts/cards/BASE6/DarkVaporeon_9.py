from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import discard_opponent_energy_attack


card = PokemonCardDef(
    guid="73fc2601-148d-53ee-8744-a86192c981d2",
    key="BASE6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkVaporeon.Name",
    display_name="Dark Vaporeon",
    searchable_by=["Dark Vaporeon", "Stage 1", "DarkVaporeon"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="BASE6",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Attack(
            title="Bite",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
        ),
        Attack(
            title="Whirlpool",
            game_text="If the Defending Pok\u00e9mon has any Energy cards attached to it, choose 1 of them and discard it.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=discard_opponent_energy_attack(),
        ),
    ],
)
