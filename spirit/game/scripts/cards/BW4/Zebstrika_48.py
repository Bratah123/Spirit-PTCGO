from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="279caedb-d05b-5842-9f42-53b6e9e6aebd",
    key="BW4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zebstrika.Name",
    display_name="Zebstrika",
    searchable_by=["Zebstrika", "Stage 1", "Zebstrika"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="BW4",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Blitzle.Name",
    family_id=522,
    abilities=[
        Attack(
            title="Disconnect",
            game_text="Your opponent can't play any Item cards from his or her hand during your opponent's next turn.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=unimplemented,
        ),
        Attack(
            title="Lightning Crash",
            game_text="Discard all Lightning Energy attached to this Pok\u00e9mon. This attack does 80 damage to 1 of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)