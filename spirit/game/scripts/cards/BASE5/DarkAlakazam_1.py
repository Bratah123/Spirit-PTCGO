from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.ecard import no_weakness_or_resistance
from spirit.game.card_effects.support_common import switch_self_attack


card = PokemonCardDef(
    guid="466214d7-f3b2-5453-ae18-e4d9cd7c7730",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkAlakazam.Name",
    display_name="Dark Alakazam",
    searchable_by=["Dark Alakazam", "Stage 2", "DarkAlakazam"],
    subtypes=["Stage 2"],
    collector_number=1,
    set_code="BASE5",
    rarity=Rarities.RareHolo,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.DarkKadabra.Name",
    family_id=63,
    abilities=[
        Attack(
            title="Teleport Blast",
            game_text="You may switch Dark Alakazam with 1 of your Benched Pok\u00e9mon. (Do the damage before switching the Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=switch_self_attack(optional=True),
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=40,
            effect=no_weakness_or_resistance,
        ),
    ],
)
