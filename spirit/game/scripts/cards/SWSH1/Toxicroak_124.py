from spirit.game.card_effects.pokemon import more_poison
from spirit.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5ba53c61-dc4c-5619-bcc8-ea283c54e746",
    key="SWSH1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Toxicroak.Name",
    display_name="Toxicroak",
    searchable_by=["Toxicroak", "Stage 1", "Toxicroak"],
    subtypes=["Stage 1"],
    collector_number=124,
    set_code="SWSH1",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Croagunk.Name",
    family_id=453,
    abilities=[
        Ability(
            title="More Poison",
            game_text="Put 2 more damage counters on your opponent's Poisoned Pok\u00e9mon during Pok\u00e9mon Checkup.",
            trigger=Triggers.BETWEEN_TURNS,
            effect=more_poison,
        ),
        Attack(
            title="Poison Claws",
            game_text="Flip a coin. If heads, your opponent's Active Pok\u00e9mon is now Poisoned.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=unimplemented,
        ),
    ],
)