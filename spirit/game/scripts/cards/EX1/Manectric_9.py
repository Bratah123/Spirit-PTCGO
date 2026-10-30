from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.attacks_common import flip_damage
from spirit.game.card_effects.pokemon import is_lightning_energy
from spirit.game.card_effects.support_common import search_attach_energy


card = PokemonCardDef(
    guid="fc8aad3f-8488-565e-9912-998803e5b1d2",
    key="EX1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Manectric.Name",
    display_name="Manectric",
    searchable_by=["Manectric", "Stage 1", "Manectric"],
    subtypes=["Stage 1"],
    collector_number=9,
    set_code="EX1",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Electrike.Name",
    family_id=309,
    abilities=[
        Attack(
            title="Attract Current",
            game_text="Search your deck for a Lightning Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=search_attach_energy(
                predicate=is_lightning_energy, count=1, distribute=False),
        ),
        Attack(
            title="Thunder Jolt",
            game_text="Flip a coin. If tails, Manectric does 10 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=flip_damage(tails_self_damage=10),
        ),
    ],
)
