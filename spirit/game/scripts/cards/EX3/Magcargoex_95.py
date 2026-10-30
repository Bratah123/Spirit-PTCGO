"""STUB: effect not implemented — do not guess mechanics.
Magcargo ex (EX3 #95): one or more attacks/abilities use effect=unimplemented until a matching prefab or known script exists.
"""

from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ex import melting_mountain, lava_flow

card = PokemonCardDef(
    guid="2bc3e705-afe2-57be-9111-677a3e445566",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Magcargoex.Name",
    display_name="Magcargo ex",
    searchable_by=["Magcargo ex", "Stage 1", "ex", "Magcargoex"],
    subtypes=["Stage 1", "ex"],
    collector_number=95,
    set_code="EX3",
    rarity=Rarities.RareHoloEX,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Slugma.Name",
    family_id=218,
    abilities=[
        Attack(
            title="Melting Mountain",
            game_text="Discard the top card from your deck. If that card is a basic Energy card, attach it to Magcargo ex.",
            cost={PokemonTypes.FIRE: 1},
            damage=20,
            # STUB: attack effect not implemented
            effect=melting_mountain(),
        ),
        Attack(
            title="Lava Flow",
            game_text="You may discard any number of basic Energy cards attached to Magcargo ex when you use this attack. If you do, this attack does 40 damage plus 20 more damage for each basic Energy card you discarded.",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="+",
            # STUB: attack effect not implemented
            effect=lava_flow(40, 20),
        ),
    ],
)