from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities, AbilityTypes
from spirit.game.card_effects.ecard import unown_perform_passive


card = PokemonCardDef(
    guid="66fc955e-67e1-5aa5-af7a-08f72b239231",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.UnownP.Name",
    display_name="Unown [P]",
    searchable_by=["Unown [P]", "Basic", "UnownP"],
    subtypes=["Basic"],
    collector_number=58,
    set_code="NEO4",
    rarity=Rarities.Uncommon,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=201,
    abilities=[
        Ability(
            title="[Perform]",
            game_text="If an attack damaged Unown [P] during your opponent's last turn and Unown [P] was your Active Pok\u00e9mon, Unown [P]'s Hidden Power attack does that much more damage to the Defending Pok\u00e9mon. This power can be used even if Unown [P] is Confused.",
            ability_type=AbilityTypes.POKE_POWER,
            passive=unown_perform_passive,
        ),
        Attack(
            title="Hidden Power",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=10,
        ),
    ],
)
