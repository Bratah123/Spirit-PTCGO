from spirit.game.card_effects.pokemon import (
    summoning_star,
    summoning_star_condition,
    tempest_dive,
)
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="03ef5e0c-e166-56af-9dd9-3fc40b576f39",
    key="SWSH12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaVSTAR.Name",
    display_name="Lugia VSTAR",
    searchable_by=["Lugia VSTAR", "VSTAR", "LugiaVSTAR"],
    subtypes=["VSTAR"],
    collector_number=139,
    set_code="SWSH12",
    rarity=Rarities.RareHoloVSTAR,
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
            game_text="During your turn, you may put up to 2 Colorless Pokémon that don't have a Rule Box from your discard pile onto your Bench. (Pokémon V, Pokémon-GX, etc. have Rule Boxes.) (You can't use more than 1 VSTAR Power in a game.)",
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
