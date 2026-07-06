from spirit.game.card_effects.pokemon import (
    summoning_star,
    summoning_star_condition,
    tempest_dive,
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8a5abc60-3d4b-5564-b8d1-adbb0e15b021",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaVSTAR.Name",
    display_name="Lugia VSTAR",
    searchable_by=["Lugia VSTAR", "VSTAR", "LugiaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=211,
    set_code="SWSH12",
    rarity=Rarities.RareSecret,
    hp=280,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.VSTAR,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaV.Name",
    family_id=249,
    abilities=[
        Ability(
            title="Summoning Star",
            game_text="During your turn, you may put up to 2 Colorless Pok\u00e9mon that don't have a Rule Box from your discard pile onto your Bench. (Pok\u00e9mon V, Pok\u00e9mon-GX, etc. have Rule Boxes.) (You can't use more than 1 VSTAR Power in a game.)",
            activation=Activations.ONCE_PER_TURN,
            vstar=True,
            effect=summoning_star,
            condition=summoning_star_condition,
        ),
        Attack(
            title="Tempest Dive",
            game_text="You may discard a Stadium in play.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=220,
            effect=tempest_dive,
        ),
    ],
)