from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.sm7 import (
    dwindling_wave,
)

card = PokemonCardDef(
    guid="bd562dc7-a3a6-545e-9ccf-3fb55167edb7",
    key="SM7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wailord.Name",
    display_name="Wailord",
    searchable_by=["Wailord", "Stage 1", "Wailord"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="SM7",
    rarity=Rarities.Rare,
    hp=220,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wailmer.Name",
    family_id=320,
    abilities=[
        Attack(
            title="Dwindling Wave",
            game_text="This attack does 40 less damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 4},
            damage=200,
            damage_operator="-",
            effect=dwindling_wave,
        ),
    ],
)