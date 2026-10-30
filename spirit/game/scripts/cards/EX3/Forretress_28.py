from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import place_counters
from spirit.game.card_effects.ex import backspin

card = PokemonCardDef(
    guid="b9bee763-7217-58d3-8638-1b73c5c053d0",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name",
    display_name="Forretress",
    searchable_by=["Forretress", "Stage 1", "Forretress"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="EX3",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name",
    family_id=204,
    abilities=[
        Attack(
            title="Double Metal Ball",
            game_text="Put 2 damage counters on each Defending Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            # STUB: attack effect not implemented
            effect=place_counters(2, target="opponent_active"),
        ),
        Attack(
            title="Backspin",
            game_text="After your attack, you may discard 1 Energy card attached to Forretress. If you do, switch Forretress with 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            # STUB: attack effect not implemented
            effect=backspin(),
        ),
    ],
)