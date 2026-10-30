"""STUB: effect not implemented — do not guess mechanics.
Dragonair δ (EX11 #42): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import twister_attack


card = PokemonCardDef(
    guid="0c2162af-6bf1-59f4-ab83-78a89bb63af8",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dragonair.Name",
    display_name="Dragonair δ",
    searchable_by=["Dragonair \u03b4", "Stage 1", "Dragonair"],
    subtypes=["Stage 1"],
    collector_number=42,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.COLORLESS,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Dratini.Name",
    family_id=148,
    abilities=[
        Attack(
            title="Twister",
            game_text="Flip 2 coins. If both are tails, this attack does nothing. For each heads, discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=twister_attack(),
        ),
    ],
)