from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes

card = PokemonCardDef(
    guid="c1fc68e0-bf75-58f5-b996-62812748985a",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cofagrigus.Name",
    display_name="Cofagrigus",
    searchable_by=["Cofagrigus", "Stage 1", "Team Plasma", "Cofagrigus"],
    subtypes=["Stage 1", "Team Plasma"],
    collector_number=56,
    set_code="BW9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yamask.Name",
    family_id=562,
    abilities=[
        Ability(
            title="Six Feet Under",
            game_text="Once during your turn (before your attack) you may Knock Out this Pok\u00e9mon. If you do, put 3 damage counters on your opponent's Pok\u00e9mon in any way you like.",
            ability_type=AbilityTypes.POKE_ABILITY,
            effect=unimplemented,
        ),
        Attack(
            title="Slap of Misfortune",
            game_text="Whenever your opponent flips a coin during his or her next turn, treat it as tails.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=unimplemented,
        ),
    ],
)