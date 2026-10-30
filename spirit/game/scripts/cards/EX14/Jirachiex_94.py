from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ex import shield_beam_block_powers_next, star_light_retreat_zero

card = PokemonCardDef(
    guid="d8b0ecbb-1f2d-536e-8f5b-9f889c4adfc0",
    key="EX14",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Jirachiex.Name",
    display_name="Jirachi ex",
    searchable_by=["Jirachi ex", "Basic", "ex", "Jirachiex"],
    subtypes=["Basic", "ex"],
    collector_number=94,
    set_code="EX14",
    rarity=Rarities.RareHoloEX,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=385,
    abilities=[
        Ability(
            title="Star Light",
            game_text="As long as your opponent has any Pok\u00e9mon-ex or Stage 2 Evolved Pok\u00e9mon in play, Jirachi ex pays Colorless less Energy to use Shield Beam or Super Psy Bolt.",
            ability_type=AbilityTypes.POKE_BODY,
            passive=star_light_retreat_zero(),
            effect=None,
        ),
        Attack(
            title="Shield Beam",
            game_text="During your opponent's next turn, your opponent can't use any Pok\u00e9-Powers on his or her Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
                        effect=shield_beam_block_powers_next(),
        ),
        Attack(
            title="Super Psy Bolt",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=50,
        ),
    ],
)