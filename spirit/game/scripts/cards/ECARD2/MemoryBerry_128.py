"""Memory Berry: holder may use attacks from Basic / prior Evolution cards in its stack."""
from spirit.game.data_utils import PokemonToolCardDef, def_for
from spirit.game.attributes import Rarities, TrainerType, AttrID
from spirit.game.session.passives import Passive, carrier_pokemon
from spirit.game.content.definitions import Attack

class MemoryBerryPassive(Passive):
    def granted_attacks(self, board, pokemon, carrier):
        if carrier_pokemon(carrier) is not pokemon:
            return []
        # Prior cards in the evolution stack (children that are pokemon cards under it,
        # or the evolves-from chain recorded on the entity). Prefer full_stack.
        from spirit.game.session.effects import full_stack
        attacks = []
        seen = set()
        # Attacks already on the current card shouldn't be re-granted.
        current_def = def_for(pokemon.archetype_id)
        current_titles = {a.title for a in (current_def.abilities or []) if isinstance(a, Attack)}
        for prior in full_stack(pokemon)[1:]:  # skip top (current)
            d = def_for(prior.archetype_id)
            if d is None:
                continue
            for a in d.abilities or []:
                if isinstance(a, Attack) and a.title not in current_titles and a.title not in seen:
                    seen.add(a.title)
                    attacks.append(a)
        return attacks

card = PokemonToolCardDef(
    guid="9180b0d8-86ed-5a87-9d2d-5835854f425f",
    key="ECARD2",
    name="com.direwolfdigital.cake.data.archetypes.trainer.MemoryBerry.Name",
    display_name="Memory Berry",
    searchable_by=["Memory Berry", "Pokémon Tool"],
    subtypes=["Pokémon Tool"],
    collector_number=128,
    set_code="ECARD2",
    rarity=Rarities.Uncommon,
    passive=MemoryBerryPassive(),
)
# Discard at end of any turn the Pokémon attacks — handled via session attack hook later if needed.
